import FWCore.ParameterSet.Config as cms

def CandCandAssociationMapOneToOne2Association(*args, **kwargs):
  mod = cms.EDProducer('CandCandAssociationMapOneToOne2Association',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
