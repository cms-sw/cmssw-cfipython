import FWCore.ParameterSet.Config as cms

candPtrProjector = cms.EDProducer('CandPtrProjector',
  useDeltaRforFootprint = cms.bool(False)
)
