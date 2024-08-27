import FWCore.ParameterSet.Config as cms

def PATObjectCrossLinker(**kwargs):
  mod = cms.EDProducer('PATObjectCrossLinker',
    jets = cms.required.InputTag,
    muons = cms.required.InputTag,
    electrons = cms.required.InputTag,
    photons = cms.required.InputTag,
    taus = cms.required.InputTag,
    lowPtElectrons = cms.InputTag(''),
    boostedTaus = cms.InputTag(''),
    vertices = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
