import FWCore.ParameterSet.Config as cms

def GEMCSCCoincidenceRateAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GEMCSCCoincidenceRateAnalyzer',
    ohStatusTag = cms.untracked.InputTag('muonGEMDigis', 'OHStatus'),
    vfatStatusTag = cms.untracked.InputTag('muonGEMDigis', 'VFATStatus'),
    logCategory = cms.untracked.string('GEMCSCCoincidenceRateAnalyzer'),
    gemcscSegmentTag = cms.untracked.InputTag('gemcscSegments'),
    muonTag = cms.untracked.InputTag('muons'),
    useGEMDAQStatus = cms.untracked.bool(False),
    cscWhitelist = cms.untracked.vuint32(
      2,
      5
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
