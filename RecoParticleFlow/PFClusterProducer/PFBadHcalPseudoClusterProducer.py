import FWCore.ParameterSet.Config as cms

def PFBadHcalPseudoClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('PFBadHcalPseudoClusterProducer',
    enable = cms.bool(True),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
