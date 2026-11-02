import FWCore.ParameterSet.Config as cms

def HGCalRecHitDQM(*args, **kwargs):
  mod = cms.EDProducer('HGCalRecHitDQM',
    RecHits = cms.InputTag('hgcalRecHits'),
    MinimumEvents = cms.uint32(5000),
    PrescaleFactor = cms.uint32(5000),
    isSimulation = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
