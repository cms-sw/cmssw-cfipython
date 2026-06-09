import FWCore.ParameterSet.Config as cms

def HGCGeometryCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCGeometryCheck',
    geometrySource = cms.untracked.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive',
      'HGCalHEScintillatorSensitive'
    ),
    g4Source = cms.InputTag('g4SimHits', 'HGCalInfoLayer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
