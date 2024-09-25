import FWCore.ParameterSet.Config as cms

def PFNuclearProducer(*args, **kwargs):
  mod = cms.EDProducer('PFNuclearProducer',
    likelihoodCut = cms.double(0.1),
    nuclearColList = cms.VInputTag('firstnuclearInteractionMaker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
