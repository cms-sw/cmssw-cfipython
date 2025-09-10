import FWCore.ParameterSet.Config as cms

def ZElectronsSelectorAndSkim(*args, **kwargs):
  mod = cms.EDFilter('ZElectronsSelectorAndSkim',
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
    eleID = cms.PSet(
      full5x5_sigmaIEtaIEtaCut = cms.vdouble(
        0.0128,
        0.0445
      ),
      dEtaInSeedCut = cms.vdouble(
        0.00523,
        0.00984
      ),
      dPhiInCut = cms.vdouble(
        0.159,
        0.157
      ),
      hOverECut = cms.vdouble(
        0.247,
        0.0982
      ),
      relCombIsolationWithEACut = cms.vdouble(
        0.168,
        0.185
      ),
      EInverseMinusPInverseCut = cms.vdouble(
        0.193,
        0.0962
      ),
      missingHitsCut = cms.vint32(
        2,
        3
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
