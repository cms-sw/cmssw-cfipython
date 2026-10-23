import FWCore.ParameterSet.Config as cms

def LHETablesProducer(*args, **kwargs):
  mod = cms.EDProducer('LHETablesProducer',
    lheInfo = cms.VInputTag(
      'externalLHEProducer',
      'source'
    ),
    precision = cms.int32(-1),
    storeLHEParticles = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
