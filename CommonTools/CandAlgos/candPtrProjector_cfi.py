import FWCore.ParameterSet.Config as cms

candPtrProjector = cms.EDProducer('CandPtrProjector',
  src = cms.required.InputTag,
  veto = cms.required.InputTag,
  useDeltaRforFootprint = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
