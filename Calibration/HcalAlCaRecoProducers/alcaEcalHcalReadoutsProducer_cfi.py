import FWCore.ParameterSet.Config as cms

alcaEcalHcalReadoutsProducer = cms.EDProducer('AlCaEcalHcalReadoutsProducer',
  hbheInput = cms.InputTag('hbhereco'),
  hfInput = cms.InputTag('hfreco'),
  hoInput = cms.InputTag('horeco'),
  mightGet = cms.optional.untracked.vstring
)
