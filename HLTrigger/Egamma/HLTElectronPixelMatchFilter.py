import FWCore.ParameterSet.Config as cms

def HLTElectronPixelMatchFilter(**kwargs):
  mod = cms.EDFilter('HLTElectronPixelMatchFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltEgammaHcalIsolFilter'),
    l1PixelSeedsTag = cms.InputTag('electronPixelSeeds'),
    npixelmatchcut = cms.double(1),
    ncandcut = cms.int32(1),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2I = cms.double(0.0007),
    s_a_phi2F = cms.double(0.00906),
    s_a_zB = cms.double(0.012),
    s_a_rI = cms.double(0.027),
    s_a_rF = cms.double(0.04),
    s2_threshold = cms.double(0),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10InterThres = cms.double(1),
    tanhSO10ForwardThres = cms.double(1),
    useS = cms.bool(False),
    pixelVeto = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod