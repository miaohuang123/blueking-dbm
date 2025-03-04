package cmd

import (
	"dbm-services/mysql/db-tools/mysql-dbbackup/pkg/src/backupexe"
	"dbm-services/mysql/db-tools/mysql-dbbackup/pkg/src/logger"
	"dbm-services/mysql/db-tools/mysql-dbbackup/pkg/src/parsecnf"

	"github.com/spf13/cobra"
)

func init() {
	// loadCmd
	loadCmd.Flags().StringVarP(&cnfFile, "config", "c", "", "one config file to load")
	_ = loadCmd.MarkFlagRequired("config")
}

var loadCmd = &cobra.Command{
	Use:   "loadbackup",
	Short: "Run load backup",
	Long:  `Run load backup using config, include logical and physical`,
	RunE: func(cmd *cobra.Command, args []string) error {
		var cnf = parsecnf.Cnf{}
		if err := initConfig(cnfFile, &cnf); err != nil {
			return err
		}
		err := loadData(&cnf)
		if err != nil {
			logger.Log.Error("Load Dbbackup: Failure")
			return err
		}
		return nil
	},
}

func loadData(cnf *parsecnf.Cnf) error {
	exeErr := backupexe.ExecuteLoad(cnf)
	if exeErr != nil {
		return exeErr
	}
	logger.Log.Info("Load Success")
	return nil
}
