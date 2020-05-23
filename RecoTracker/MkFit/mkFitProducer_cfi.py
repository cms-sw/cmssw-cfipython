import FWCore.ParameterSet.Config as cms

mkFitProducer = cms.EDProducer('MkFitProducer',
  hitsSeeds = cms.InputTag('mkFitInputConverter'),
  buildingRoutine = cms.string('cloneEngine'),
  seedCleaning = cms.string('N2'),
  backwardFitInCMSSW = cms.bool(False),
  mkFitSilent = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
