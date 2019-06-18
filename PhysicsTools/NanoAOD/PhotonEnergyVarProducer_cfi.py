import FWCore.ParameterSet.Config as cms

PhotonEnergyVarProducer = cms.EDProducer('PhotonEnergyVarProducer',
  srcRaw = cms.required.InputTag,
  srcCorr = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
