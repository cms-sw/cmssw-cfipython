import FWCore.ParameterSet.Config as cms

def PFBadHcalPseudoClusterProducer(**kwargs):
  mod = cms.EDProducer('PFBadHcalPseudoClusterProducer',
    enable = cms.bool(True),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
