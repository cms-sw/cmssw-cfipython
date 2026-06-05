import FWCore.ParameterSet.Config as cms

def EleIdCutBased(*args, **kwargs):
  mod = cms.EDFilter('EleIdCutBased',
    src = cms.InputTag(''),
    threshold = cms.double(-1),
    algorithm = cms.string(''),
    electronIDType = cms.string('classbased'),
    electronQuality = cms.string('loose'),
    electronVersion = cms.string('V06'),
    additionalCategories = cms.bool(False),
    etBinning = cms.bool(False),
    classbasedLooseEleIDCutsV06 = cms.PSet(
      hOverE = cms.vdouble(),
      sigmaEtaEta = cms.vdouble(),
      deltaPhiIn = cms.vdouble(),
      deltaEtaIn = cms.vdouble(),
      eSeedOverPin = cms.vdouble(),
      cutiso_sum = cms.vdouble(),
      cutiso_sumoet = cms.vdouble(),
      cutfmishits = cms.vdouble(),
      cutdcotdist = cms.vdouble(),
      cutip_gsf = cms.vdouble()
    ),
    classbasedTightEleIDCutsV06 = cms.PSet(
      hOverE = cms.vdouble(),
      sigmaEtaEta = cms.vdouble(),
      deltaPhiIn = cms.vdouble(),
      deltaEtaIn = cms.vdouble(),
      eSeedOverPin = cms.vdouble(),
      cutiso_sum = cms.vdouble(),
      cutiso_sumoet = cms.vdouble(),
      cutfmishits = cms.vdouble(),
      cutdcotdist = cms.vdouble(),
      cutip_gsf = cms.vdouble()
    ),
    robustLooseEleIDCuts = cms.PSet(
      barrel = cms.vdouble(),
      endcap = cms.vdouble()
    ),
    robustTightEleIDCuts = cms.PSet(
      barrel = cms.vdouble(),
      endcap = cms.vdouble()
    ),
    verticesCollection = cms.InputTag('offlinePrimaryVertices'),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
