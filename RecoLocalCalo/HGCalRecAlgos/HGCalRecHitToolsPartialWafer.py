import FWCore.ParameterSet.Config as cms

def HGCalRecHitToolsPartialWafer(**kwargs):
  mod = cms.EDAnalyzer('HGCalRecHitToolsPartialWafer',
    source = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    nameSense = cms.string('HGCalEESensitive'),
    checkDigi = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
