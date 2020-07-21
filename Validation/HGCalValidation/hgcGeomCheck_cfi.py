import FWCore.ParameterSet.Config as cms

hgcGeomCheck = cms.EDAnalyzer('HGCGeometryCheck',
  geometrySource = cms.untracked.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'HGCalHEScintillatorSensitive'
  ),
  g4Source = cms.InputTag('g4SimHits', 'HGCalInfoLayer'),
  mightGet = cms.optional.untracked.vstring
)
