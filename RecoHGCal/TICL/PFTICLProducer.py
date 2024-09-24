import FWCore.ParameterSet.Config as cms

def PFTICLProducer(*args, **kwargs):
  mod = cms.EDProducer('PFTICLProducer',
    ticlCandidateSrc = cms.InputTag('ticlTrackstersMerge'),
    trackTimeValueMap = cms.InputTag('tofPID', 't0'),
    trackTimeErrorMap = cms.InputTag('tofPID', 'sigmat0'),
    trackTimeQualityMap = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    energyFromRegression = cms.bool(True),
    timingQualityThreshold = cms.double(0.5),
    useMTDTiming = cms.bool(True),
    isTICLv5 = cms.bool(False),
    useTimingAverage = cms.bool(False),
    muonSrc = cms.InputTag('muons1stStep'),
    pfMuonAlgoParameters = cms.PSet(
      maxDPtOPt = cms.double(1),
      trackQuality = cms.string('highPurity'),
      ptErrorScale = cms.double(8),
      eventFractionForCleaning = cms.double(0.5),
      minPtForPostCleaning = cms.double(20),
      eventFactorForCosmics = cms.double(10),
      metSignificanceForCleaning = cms.double(3),
      metSignificanceForRejection = cms.double(4),
      metFactorForCleaning = cms.double(4),
      eventFractionForRejection = cms.double(0.8),
      metFactorForRejection = cms.double(4),
      metFactorForHighEta = cms.double(25),
      ptFactorForHighEta = cms.double(2),
      metFactorForFakes = cms.double(4),
      minMomentumForPunchThrough = cms.double(100),
      minEnergyForPunchThrough = cms.double(100),
      punchThroughFactor = cms.double(3),
      punchThroughMETFactor = cms.double(4),
      cosmicRejectionDistance = cms.double(1)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
