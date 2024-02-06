import FWCore.ParameterSet.Config as cms

EvFFEDExcluder = cms.EDProducer('EvFFEDExcluder',
  src = cms.InputTag('source'),
  fedsToExclude = cms.vuint32(),
  mightGet = cms.optional.untracked.vstring
)
