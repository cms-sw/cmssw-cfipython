import FWCore.ParameterSet.Config as cms

AlpakaServiceCudaAsync = cms.Service('AlpakaServiceCudaAsync',
  enabled = cms.untracked.bool(True),
  verbose = cms.untracked.bool(False)
)
