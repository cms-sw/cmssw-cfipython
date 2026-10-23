import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationPCLHarvester(*args, **kwargs):
  mod = cms.EDProducer('PPSTimingCalibrationPCLHarvester',
    dqmDir = cms.string('AlCaReco/PPSTimingCalibrationPCL'),
    formula = cms.string('[0]/(exp((x-[1])/[2])+1)+[3]'),
    minEntries = cms.uint32(100),
    thresholdFractionOfMax = cms.double(0.05),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
