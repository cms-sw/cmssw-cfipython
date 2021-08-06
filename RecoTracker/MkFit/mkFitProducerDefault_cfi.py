import FWCore.ParameterSet.Config as cms

mkFitProducerDefault = cms.EDProducer('MkFitProducer',
  pixelHits = cms.InputTag('mkFitSiPixelHits'),
  stripHits = cms.InputTag('mkFitSiStripHits'),
  eventOfHits = cms.InputTag('mkFitEventOfHits'),
  seeds = cms.InputTag('mkFitSeedConverter'),
  clustersToSkip = cms.InputTag(''),
  buildingRoutine = cms.string('cloneEngine'),
  config = cms.required.ESInputTag,
  seedCleaning = cms.bool(True),
  removeDuplicates = cms.bool(True),
  backwardFitInCMSSW = cms.bool(False),
  mkFitSilent = cms.untracked.bool(True),
  limitConcurrency = cms.untracked.bool(False),
  minGoodStripCharge = cms.PSet(
    value = cms.required.double
  ),
  mightGet = cms.optional.untracked.vstring
)