import FWCore.ParameterSet.Config as cms

AlpakaServiceSerialSync = cms.Service('AlpakaServiceSerialSync',
  enabled = cms.untracked.bool(True),
  verbose = cms.untracked.bool(False)
)
