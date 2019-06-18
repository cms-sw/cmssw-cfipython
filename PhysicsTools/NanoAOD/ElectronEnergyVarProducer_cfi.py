import FWCore.ParameterSet.Config as cms

ElectronEnergyVarProducer = cms.EDProducer('ElectronEnergyVarProducer',
  srcRaw = cms.required.InputTag,
  srcCorr = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
