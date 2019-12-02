import FWCore.ParameterSet.Config as cms

EnergyRingsTable = cms.EDProducer('EnergyRingsTableProducer',
  src = cms.required.InputTag,
  name = cms.required.string,
  mightGet = cms.optional.untracked.vstring
)
