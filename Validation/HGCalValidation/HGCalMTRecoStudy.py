import FWCore.ParameterSet.Config as cms

def HGCalMTRecoStudy(**kwargs):
  mod = cms.EDAnalyzer('HGCalMTRecoStudy',
    detectorName = cms.string('HGCalEESensitive'),
    source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    layerList = cms.string('1'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
