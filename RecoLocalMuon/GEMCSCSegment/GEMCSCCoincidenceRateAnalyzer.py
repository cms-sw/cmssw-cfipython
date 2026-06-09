import FWCore.ParameterSet.Config as cms

def GEMCSCCoincidenceRateAnalyzer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
