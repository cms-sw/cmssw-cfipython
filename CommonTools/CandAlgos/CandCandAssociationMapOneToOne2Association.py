import FWCore.ParameterSet.Config as cms

def CandCandAssociationMapOneToOne2Association(**kwargs):
  mod = cms.EDProducer('CandCandAssociationMapOneToOne2Association',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
