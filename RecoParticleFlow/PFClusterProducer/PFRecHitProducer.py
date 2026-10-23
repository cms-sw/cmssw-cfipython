import FWCore.ParameterSet.Config as cms

def PFRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('PFRecHitProducer',
    navigator = cms.PSet(
      name = cms.string(''),
      hcalEnums = cms.vint32(),
      barrel = cms.PSet(),
      endcap = cms.PSet(),
      hgcee = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      ),
      hgcheb = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      ),
      hgchef = cms.PSet(
        name = cms.string(''),
        topologySource = cms.string('')
      )
    ),
    producers = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.string(''),
        src = cms.InputTag(''),
        qualityTests = cms.VPSet(
          template = cms.PSetTemplate(
            name = cms.string(''),
            maxSeverities = cms.vint32(),
            cleaningThresholds = cms.vdouble(),
            flags = cms.vstring(),
            usePFThresholdsFromDB = cms.bool(False),
            cuts = cms.VPSet(
              template = cms.PSetTemplate(
                depth = cms.vint32(),
                threshold = cms.vdouble(),
                detectorEnum = cms.int32(0)
              )
            ),
            thresholdSNR = cms.double(0),
            applySelectionsToAllCrystals = cms.bool(False),
            cleaningThreshold = cms.double(0),
            timingCleaning = cms.bool(False),
            topologicalCleaning = cms.bool(False),
            skipTTRecoveredHits = cms.bool(False),
            threshold = cms.double(0),
            threshold_ring0 = cms.double(0),
            threshold_ring12 = cms.double(0)
          )
        ),
        EMDepthCorrection = cms.double(0),
        HADDepthCorrection = cms.double(0),
        thresh_HF = cms.double(0),
        ShortFibre_Cut = cms.double(0),
        LongFibre_Fraction = cms.double(0),
        LongFibre_Cut = cms.double(0),
        ShortFibre_Fraction = cms.double(0),
        HFCalib29 = cms.double(0),
        srFlags = cms.InputTag(''),
        geometryInstance = cms.string('')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
