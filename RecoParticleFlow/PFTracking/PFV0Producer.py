import FWCore.ParameterSet.Config as cms

def PFV0Producer(**kwargs):
  mod = cms.EDProducer('PFV0Producer',
    V0List = cms.VInputTag(
      'generalV0Candidates:Kshort',
      'generalV0Candidates:Lambda'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
