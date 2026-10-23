import FWCore.ParameterSet.Config as cms

def RecoTauPiZeroUnembedder(*args, **kwargs):
  mod = cms.EDProducer('RecoTauPiZeroUnembedder',
    src = cms.InputTag('hpsPFTauProducerSansRefs'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
