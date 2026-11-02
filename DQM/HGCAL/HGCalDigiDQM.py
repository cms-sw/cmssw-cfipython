import FWCore.ParameterSet.Config as cms

def HGCalDigiDQM(*args, **kwargs):
  mod = cms.EDProducer('HGCalDigiDQM',
    Digis = cms.InputTag('hgcalDigis'),
    MinimumEvents = cms.uint32(5000),
    PrescaleFactor = cms.uint32(5000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
