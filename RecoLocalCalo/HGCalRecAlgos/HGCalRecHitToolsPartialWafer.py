import FWCore.ParameterSet.Config as cms

def HGCalRecHitToolsPartialWafer(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalRecHitToolsPartialWafer',
    source = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    nameSense = cms.string('HGCalEESensitive'),
    checkDigi = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
