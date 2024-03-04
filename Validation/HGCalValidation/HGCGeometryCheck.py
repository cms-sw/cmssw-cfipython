import FWCore.ParameterSet.Config as cms

def HGCGeometryCheck(**kwargs):
  mod = cms.EDAnalyzer('HGCGeometryCheck',
    geometrySource = cms.untracked.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive',
      'HGCalHEScintillatorSensitive'
    ),
    g4Source = cms.InputTag('g4SimHits', 'HGCalInfoLayer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
