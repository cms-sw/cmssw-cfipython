import FWCore.ParameterSet.Config as cms

def HLTEgammaCaloIsolFilterPairs(*args, **kwargs):
  mod = cms.EDFilter('HLTEgammaCaloIsolFilterPairs',
    saveTags = cms.bool(True),
    candTag = cms.InputTag(''),
    isoTag = cms.InputTag(''),
    nonIsoTag = cms.InputTag(''),
    isolcutEB1 = cms.double(0),
    IsoOverEtCutEB1 = cms.double(0),
    IsoOverEt2CutEB1 = cms.double(0),
    isolcutEE1 = cms.double(0),
    IsoOverEtCutEE1 = cms.double(0),
    IsoOverEt2CutEE1 = cms.double(0),
    isolcutEB2 = cms.double(0),
    IsoOverEtCutEB2 = cms.double(0),
    IsoOverEt2CutEB2 = cms.double(0),
    isolcutEE2 = cms.double(0),
    IsoOverEtCutEE2 = cms.double(0),
    IsoOverEt2CutEE2 = cms.double(0),
    AlsoNonIso1 = cms.bool(False),
    AlsoNonIso2 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
