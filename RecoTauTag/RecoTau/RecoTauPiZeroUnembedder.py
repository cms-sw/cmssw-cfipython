import FWCore.ParameterSet.Config as cms

def RecoTauPiZeroUnembedder(**kwargs):
  mod = cms.EDProducer('RecoTauPiZeroUnembedder',
    src = cms.InputTag('hpsPFTauProducerSansRefs'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
