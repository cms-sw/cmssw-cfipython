import FWCore.ParameterSet.Config as cms

def MkFitFitProducer(*args, **kwargs):
  mod = cms.EDProducer('MkFitFitProducer',
    eventOfHits = cms.InputTag('mkFitEventOfHits'),
    config = cms.ESInputTag('', ''),
    pixelCPE = cms.string('PixelCPETemplateReco'),
    mkFitPixelHits = cms.InputTag('mkFitSiPixelHits'),
    tracks = cms.InputTag('mkFitProducer'),
    mkFitSilent = cms.untracked.bool(True),
    limitConcurrency = cms.untracked.bool(False),
    candCutSel = cms.bool(False),
    candMinPtCut = cms.double(0),
    candMinNHitsCut = cms.int32(0),
    candMinPtRelaxedCut = cms.double(0),
    candMinAbsEtaForRelaxedCut = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
