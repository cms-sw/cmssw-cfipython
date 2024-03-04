import FWCore.ParameterSet.Config as cms

def EcalSimHitDump(**kwargs):
  mod = cms.EDAnalyzer('EcalSimHitDump',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollections = cms.vstring(
      'EcalHitsEB',
      'EcalHitsEE',
      'EcalHitsES'
    ),
    CollectionTypes = cms.vint32(
      0,
      1,
      2
    ),
    MaxEvent = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
