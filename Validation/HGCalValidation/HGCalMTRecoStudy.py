import FWCore.ParameterSet.Config as cms

def HGCalMTRecoStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMTRecoStudy',
    detectorName = cms.string('HGCalEESensitive'),
    source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    layerList = cms.string('1'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
