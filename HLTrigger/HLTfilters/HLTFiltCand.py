import FWCore.ParameterSet.Config as cms

def HLTFiltCand(**kwargs):
  mod = cms.EDFilter('HLTFiltCand',
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
    MinPt = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
