import FWCore.ParameterSet.Config as cms

def IsoPhotonEBSelectorAndSkim(*args, **kwargs):
  mod = cms.EDFilter('IsoPhotonEBSelectorAndSkim',
    src = cms.InputTag(''),
    rho = cms.InputTag('fixedGridRhoFastjetCentralCalo'),
    absEtaMin = cms.vdouble(
      0,
      1,
      1.479,
      2,
      2.2,
      2.3,
      2.4
    ),
    absEtaMax = cms.vdouble(
      1,
      1.479,
      2,
      2.2,
      2.3,
      2.4,
      5
    ),
    effectiveAreaValues = cms.vdouble(
      0.1703,
      0.1715,
      0.1213,
      0.123,
      0.1635,
      0.1937,
      0.2393
    ),
    phID = cms.PSet(
      full5x5_sigmaIEtaIEtaCut = cms.vdouble(
        0.011,
        -1
      ),
      hOverECut = cms.vdouble(
        0.1,
        -1
      ),
      relCombIsolationWithEACut = cms.vdouble(
        0.05,
        -1
      )
    ),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
