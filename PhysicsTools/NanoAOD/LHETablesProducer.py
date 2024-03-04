import FWCore.ParameterSet.Config as cms

def LHETablesProducer(**kwargs):
  mod = cms.EDProducer('LHETablesProducer',
    lheInfo = cms.VInputTag(
      'externalLHEProducer',
      'source'
    ),
    precision = cms.int32(-1),
    storeLHEParticles = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
