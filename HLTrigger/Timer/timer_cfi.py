import FWCore.ParameterSet.Config as cms

timer = cms.EDProducer('Timer',
  includeSelf = cms.untracked.bool(False)
)
