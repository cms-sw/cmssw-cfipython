import FWCore.ParameterSet.Config as cms

hltFiltCand = cms.EDFilter('HLTFiltCand',
  saveTags = cms.bool(True),
  photTag = cms.InputTag('photCollection'),
  elecTag = cms.InputTag('elecCollection'),
  muonTag = cms.InputTag('muonCollection'),
  tausTag = cms.InputTag('tausCollection'),
  jetsTag = cms.InputTag('jetsCollection'),
  metsTag = cms.InputTag('metsCollection'),
  mhtsTag = cms.InputTag('mhtsCollection'),
  trckTag = cms.InputTag('trckCollection'),
  ecalTag = cms.InputTag('ecalCollection'),
  MinPt = cms.double(-1)
)
