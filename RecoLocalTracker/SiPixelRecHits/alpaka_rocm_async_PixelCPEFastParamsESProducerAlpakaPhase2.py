import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PixelCPEFastParamsESProducerAlpakaPhase2(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::PixelCPEFastParamsESProducerAlpakaPhase2',
    LoadTemplatesFromDB = cms.bool(True),
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    useLAWidthFromDB = cms.bool(True),
    lAOffset = cms.double(0),
    lAWidthBPix = cms.double(0),
    lAWidthFPix = cms.double(0),
    doLorentzFromAlignment = cms.bool(False),
    useLAFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(
      0.00115,
      0.0012,
      0.00088
    ),
    yerr_barrel_l1 = cms.vdouble(
      0.00375,
      0.0023,
      0.0025,
      0.0025,
      0.0023,
      0.0023,
      0.0021,
      0.0021,
      0.0024
    ),
    xerr_barrel_ln = cms.vdouble(
      0.00115,
      0.0012,
      0.00088
    ),
    yerr_barrel_ln = cms.vdouble(
      0.00375,
      0.0023,
      0.0025,
      0.0025,
      0.0023,
      0.0023,
      0.0021,
      0.0021,
      0.0024
    ),
    xerr_endcap = cms.vdouble(
      0.002,
      0.002
    ),
    yerr_endcap = cms.vdouble(0.0021),
    xerr_barrel_l1_def = cms.double(0.0103),
    yerr_barrel_l1_def = cms.double(0.0021),
    xerr_barrel_ln_def = cms.double(0.0103),
    yerr_barrel_ln_def = cms.double(0.0021),
    xerr_endcap_def = cms.double(0.002),
    yerr_endcap_def = cms.double(0.00075),
    EdgeClusterErrorX = cms.double(50),
    EdgeClusterErrorY = cms.double(85),
    UseErrorsFromTemplates = cms.bool(True),
    TruncatePixelCharge = cms.bool(True),
    ComponentName = cms.string('PixelCPEFastParamsPhase2'),
    MagneticFieldRecord = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
