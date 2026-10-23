import FWCore.ParameterSet.Config as cms

def PFV0Producer(*args, **kwargs):
  mod = cms.EDProducer('PFV0Producer',
    V0List = cms.VInputTag(
      'generalV0Candidates:Kshort',
      'generalV0Candidates:Lambda'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
