import FWCore.ParameterSet.Config as cms

def CaloMETProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloMETProducer',
    src = cms.InputTag('towerMaker'),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.3),
    noHF = cms.bool(False),
    alias = cms.string(''),
    EB_EtResPar = cms.vdouble(
      0.2,
      0.03,
      0.005
    ),
    EB_PhiResPar = cms.vdouble(0.00502),
    EE_EtResPar = cms.vdouble(
      0.2,
      0.03,
      0.005
    ),
    EE_PhiResPar = cms.vdouble(0.02511),
    HB_EtResPar = cms.vdouble(
      0,
      1.22,
      0.05
    ),
    HB_PhiResPar = cms.vdouble(0.02511),
    HE_EtResPar = cms.vdouble(
      0,
      1.3,
      0.05
    ),
    HE_PhiResPar = cms.vdouble(0.02511),
    HO_EtResPar = cms.vdouble(
      0,
      1.3,
      0.005
    ),
    HO_PhiResPar = cms.vdouble(0.02511),
    HF_EtResPar = cms.vdouble(
      0,
      1.82,
      0.09
    ),
    HF_PhiResPar = cms.vdouble(0.05022),
    PF_EtResType1 = cms.vdouble(
      0.05,
      0,
      0
    ),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType2 = cms.vdouble(
      0.05,
      0,
      0
    ),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_EtResType3 = cms.vdouble(
      0.05,
      0,
      0
    ),
    PF_PhiResType3 = cms.vdouble(0.002),
    PF_EtResType4 = cms.vdouble(
      0.042,
      0.1,
      0
    ),
    PF_PhiResType4 = cms.vdouble(
      0.0028,
      0,
      0.0022
    ),
    PF_EtResType5 = cms.vdouble(
      0.41,
      0.52,
      0.25
    ),
    PF_PhiResType5 = cms.vdouble(
      0.1,
      0.1,
      0.13
    ),
    PF_EtResType6 = cms.vdouble(
      0,
      1.22,
      0.05
    ),
    PF_PhiResType6 = cms.vdouble(0.02511),
    PF_EtResType7 = cms.vdouble(
      0,
      1.22,
      0.05
    ),
    PF_PhiResType7 = cms.vdouble(0.02511),
    resolutionsEra = cms.string('Spring10'),
    resolutionsAlgo = cms.string('AK5PF'),
    ptresolthreshold = cms.double(10),
    jdpt0 = cms.vdouble(),
    jdphi0 = cms.vdouble(),
    jdpt1 = cms.vdouble(),
    jdphi1 = cms.vdouble(),
    jdpt2 = cms.vdouble(),
    jdphi2 = cms.vdouble(),
    jdpt3 = cms.vdouble(),
    jdphi3 = cms.vdouble(),
    jdpt4 = cms.vdouble(),
    jdphi4 = cms.vdouble(),
    jdpt5 = cms.vdouble(),
    jdphi5 = cms.vdouble(),
    jdpt6 = cms.vdouble(),
    jdphi6 = cms.vdouble(),
    jdpt7 = cms.vdouble(),
    jdphi7 = cms.vdouble(),
    jdpt8 = cms.vdouble(),
    jdphi8 = cms.vdouble(),
    jdpt9 = cms.vdouble(),
    jdphi9 = cms.vdouble(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
