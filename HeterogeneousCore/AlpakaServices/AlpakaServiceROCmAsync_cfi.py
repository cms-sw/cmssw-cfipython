import FWCore.ParameterSet.Config as cms

AlpakaServiceROCmAsync = cms.Service('AlpakaServiceROCmAsync',
  enabled = cms.untracked.bool(True),
  verbose = cms.untracked.bool(False)
)
