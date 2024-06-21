import FWCore.ParameterSet.Config as cms

def PFNuclearProducer(**kwargs):
  mod = cms.EDProducer('PFNuclearProducer',
    likelihoodCut = cms.double(0.1),
    nuclearColList = cms.VInputTag('firstnuclearInteractionMaker'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
