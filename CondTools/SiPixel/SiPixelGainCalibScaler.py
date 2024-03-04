import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibScaler(**kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibScaler',
    record = cms.string('SiPixelGainCalibrationForHLTRcd'),
    isForHLT = cms.bool(True),
    parameters = cms.VPSet(
      cms.PSet(
        conversionFactor = cms.double(65),
        conversionFactorL1 = cms.double(65),
        offset = cms.double(-414),
        offsetL1 = cms.double(-414),
        phase = cms.uint32(0)
      ),
      cms.PSet(
        conversionFactor = cms.double(47),
        conversionFactorL1 = cms.double(50),
        offset = cms.double(-60),
        offsetL1 = cms.double(-670),
        phase = cms.uint32(1)
      )
    ),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
