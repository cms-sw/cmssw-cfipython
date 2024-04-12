import FWCore.ParameterSet.Config as cms

btvMCTable = cms.EDProducer('BTVMCFlavourTableProducer',
  src = cms.required.InputTag,
  genparticles = cms.required.InputTag,
  name = cms.required.string,
  mightGet = cms.optional.untracked.vstring
)
